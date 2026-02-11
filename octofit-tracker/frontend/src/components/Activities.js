import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Activities - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Activities - Processed data:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities - Error:', error);
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

  const getActivityIcon = (type) => {
    const icons = {
      'Running': '🏃',
      'Cycling': '🚴',
      'Swimming': '🏊',
      'Walking': '🚶',
      'Yoga': '🧘',
      'Gym': '🏋️'
    };
    return icons[type] || '💪';
  };

  return (
    <div className="container mt-5">
      <h2>🏃 Activities</h2>
      <p className="text-muted mb-4">Total activities: <span className="badge bg-primary">{activities.length}</span></p>
      <div className="table-responsive">
        <table className="table table-hover table-bordered">
          <thead>
            <tr>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Distance (km)</th>
              <th>Calories Burned</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.length > 0 ? (
              activities.map((activity) => (
                <tr key={activity.id}>
                  <td><strong>{activity.user_name || activity.user || 'N/A'}</strong></td>
                  <td>
                    {getActivityIcon(activity.activity_type)} {activity.activity_type || 'N/A'}
                  </td>
                  <td><span className="badge bg-info">{activity.duration || 0} min</span></td>
                  <td><span className="badge bg-primary">{activity.distance || 0} km</span></td>
                  <td><span className="badge bg-warning text-dark">{activity.calories_burned || 0} cal</span></td>
                  <td>{activity.date ? new Date(activity.date).toLocaleDateString() : 'N/A'}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center text-muted">No activities found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
