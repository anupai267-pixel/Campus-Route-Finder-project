# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash

from graph import get_all_locations
from bfs import bfs_shortest_path
from dijkstra import dijkstra_shortest_path
from dfs import dfs_all_paths, check_disconnected, find_reachable_locations
from auth import register_user, verify_login
from history import save_history, get_history, clear_history

app = Flask(__name__)
app.secret_key = "change-this-to-any-random-text"  # needed for login sessions + flash messages


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        success, message = register_user(username, password, confirm_password)
        if success:
            flash(message, 'success')
            return redirect(url_for('login'))
        else:
            flash(message, 'error')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        result_username, message = verify_login(username, password)
        if result_username:
            session['username'] = result_username
            return redirect(url_for('dashboard'))
        else:
            flash(message, 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    locations = get_all_locations()
    result = None

    if request.method == 'POST':
        mode = request.form.get('mode')
        start = request.form.get('start')
        end = request.form.get('end')
        avoid = request.form.get('avoid') or None

        if mode == 'bfs':
            path = bfs_shortest_path(start, end)
            if path:
                save_history(session['username'], start, end, 'BFS')
            result = {'type': 'bfs', 'path': path}

        elif mode == 'dijkstra':
            path, distance = dijkstra_shortest_path(start, end)
            if path:
                save_history(session['username'], start, end, 'Dijkstra')
            result = {'type': 'dijkstra', 'path': path, 'distance': distance}

        elif mode == 'dfs':
            paths = dfs_all_paths(start, end)
            result = {'type': 'dfs', 'paths': paths}

        elif mode == 'avoid':
            bfs_path = bfs_shortest_path(start, end, avoid=avoid)
            dij_path, dij_distance = dijkstra_shortest_path(start, end, avoid=avoid)
            result = {
                'type': 'avoid', 'avoid': avoid,
                'bfs_path': bfs_path,
                'dij_path': dij_path, 'dij_distance': dij_distance
            }

        elif mode == 'reachable':
            reachable = find_reachable_locations(start)
            reachable.discard(start)
            result = {'type': 'reachable', 'start': start, 'reachable': sorted(reachable)}

        elif mode == 'disconnected':
            report = check_disconnected()
            result = {'type': 'disconnected', 'report': report}

    return render_template(
        'dashboard.html',
        locations=locations,
        result=result,
        username=session['username']
    )


@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))
    records = get_history(session['username'])
    return render_template('history.html', records=records, username=session['username'])


@app.route('/history/clear', methods=['POST'])
def history_clear():
    if 'username' not in session:
        return redirect(url_for('login'))
    clear_history(session['username'])
    flash('Your route history has been cleared.', 'success')
    return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True)