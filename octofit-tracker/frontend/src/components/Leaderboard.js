import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard - Error:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  const getRankBadgeClass = (rank) => {
    if (rank === 1) return 'rank-badge gold';
    if (rank === 2) return 'rank-badge silver';
    if (rank === 3) return 'rank-badge bronze';
    return 'rank-badge default';
  };

  const getRankEmoji = (rank) => {
    if (rank === 1) return '🥇';
    if (rank === 2) return '🥈';
    if (rank === 3) return '🥉';
    return `#${rank}`;
  };

  return (
    <div className="container mt-5">
      <h2>🏆 Leaderboard</h2>
      <p className="text-muted mb-4">Top performers ranked by total points</p>
      <div className="table-responsive">
        <table className="table table-hover table-bordered">
          <thead>
            <tr>
              <th style={{width: '80px'}}>Rank</th>
              <th>User</th>
              <th>Total Points</th>
              <th>Total Activities</th>
              <th>Total Calories</th>
              <th>Total Distance (km)</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index}>
                  <td>
                    <div className={getRankBadgeClass(index + 1)}>
                      {getRankEmoji(index + 1)}
                    </div>
                  </td>
                  <td><strong>{entry.user_name || entry.user || 'N/A'}</strong></td>
                  <td><span className="badge bg-primary">{entry.total_points || 0} pts</span></td>
                  <td><span className="badge bg-info">{entry.total_activities || 0}</span></td>
                  <td><span className="badge bg-warning text-dark">{entry.total_calories || 0} cal</span></td>
                  <td><span className="badge bg-success">{entry.total_distance || 0} km</span></td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center text-muted">No leaderboard data found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
