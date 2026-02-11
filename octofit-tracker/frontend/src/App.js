import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofitapp-small.png" alt="OctoFit Logo" />
              <strong>OctoFit Tracker</strong>
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-5">
              <div className="jumbotron text-center">
                <h1 className="display-4">Welcome to OctoFit Tracker! 🏋️</h1>
                <p className="lead">
                  Track your fitness journey, compete with your team, and achieve your goals.
                </p>
                <hr className="my-4" />
                <p className="mb-4">
                  Get started by exploring the navigation menu above to view users, activities, teams, leaderboard, and personalized workout suggestions.
                </p>
                <div className="row mt-4">
                  <div className="col-md-3 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h5 className="card-title">👥 Users</h5>
                        <p className="card-text">View all registered users</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-3 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h5 className="card-title">🏃 Activities</h5>
                        <p className="card-text">Track fitness activities</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-3 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h5 className="card-title">🤝 Teams</h5>
                        <p className="card-text">Join and manage teams</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-3 mb-3">
                    <div className="card text-center">
                      <div className="card-body">
                        <h5 className="card-title">🏆 Leaderboard</h5>
                        <p className="card-text">See top performers</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
