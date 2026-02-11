import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error:', error);
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

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Beginner': 'bg-success',
      'Intermediate': 'bg-warning text-dark',
      'Advanced': 'bg-danger'
    };
    return badges[difficulty] || 'bg-secondary';
  };

  const getWorkoutIcon = (type) => {
    const icons = {
      'Cardio': '❤️',
      'Strength': '💪',
      'Flexibility': '🧘',
      'HIIT': '⚡',
      'Yoga': '🕉️'
    };
    return icons[type] || '🏋️';
  };

  return (
    <div className="container mt-5">
      <h2>💡 Workout Suggestions</h2>
      <p className="text-muted mb-4">Personalized workout recommendations: <span className="badge bg-primary">{workouts.length}</span></p>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">
                    {getWorkoutIcon(workout.workout_type)} {workout.name || 'Unnamed Workout'}
                  </h5>
                  <h6 className="card-subtitle mb-3">
                    <span className={`badge ${getDifficultyBadge(workout.difficulty_level)}`}>
                      {workout.difficulty_level || 'General'}
                    </span>
                    <span className="badge bg-info ms-2">{workout.workout_type || 'General'}</span>
                  </h6>
                  <p className="card-text">{workout.description || 'No description available'}</p>
                </div>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">
                    <strong>⏱️ Duration:</strong> <span className="badge bg-primary ms-2">{workout.duration || 0} minutes</span>
                  </li>
                  <li className="list-group-item">
                    <strong>🔥 Calories:</strong> <span className="badge bg-warning text-dark ms-2">{workout.estimated_calories || 0} cal</span>
                  </li>
                </ul>
                <div className="card-body">
                  <button className="btn btn-primary btn-sm w-100">Start Workout</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No workout suggestions available. Complete more activities to get personalized recommendations!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
