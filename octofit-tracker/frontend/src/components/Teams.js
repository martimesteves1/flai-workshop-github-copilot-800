import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams - Processed data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams - Error:', error);
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

  return (
    <div className="container mt-5">
      <h2>🤝 Teams</h2>
      <p className="text-muted mb-4">Total teams: <span className="badge bg-primary">{teams.length}</span></p>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team) => (
            <div key={team.id} className="col-md-4 mb-4">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">🏆 {team.name || 'Unnamed Team'}</h5>
                  <p className="card-text text-muted">{team.description || 'No description available'}</p>
                </div>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">
                    <strong>Members:</strong> <span className="badge bg-success ms-2">{team.member_count || 0}</span>
                  </li>
                  <li className="list-group-item">
                    <strong>Created:</strong> {team.created_at ? new Date(team.created_at).toLocaleDateString() : 'N/A'}
                  </li>
                </ul>
                <div className="card-body">
                  <button className="btn btn-primary btn-sm w-100">View Team</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No teams found. Create your first team!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;
