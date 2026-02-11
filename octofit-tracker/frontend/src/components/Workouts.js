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

  if (loading) return <div className="container mt-5"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-5"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-5">
      <h2>Workout Suggestions</h2>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{workout.name || 'Unnamed Workout'}</h5>
                  <h6 className="card-subtitle mb-2 text-muted">
                    {workout.workout_type || 'General'}
                  </h6>
                  <p className="card-text">{workout.description || 'No description available'}</p>
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                      <strong>Duration:</strong> {workout.duration || 0} minutes
                    </li>
                    <li className="list-group-item">
                      <strong>Difficulty:</strong> {workout.difficulty_level || 'N/A'}
                    </li>
                    <li className="list-group-item">
                      <strong>Calories:</strong> {workout.estimated_calories || 0}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <p className="text-center">No workout suggestions found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
