import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    const fetchIncidents = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/incidents');
        const data = await response.json();
        setIncidents(data);
      } catch (error) {
        console.error('Error fetching incidents:', error);
      }
    };
    fetchIncidents();
    const interval = setInterval(fetchIncidents, 5000); // Poll every 5 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard">
      <h2>Real-Time Alerts</h2>
      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>IP</th>
            <th>Event</th>
            <th>Severity</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map((incident) => (
            <tr key={incident.id} className={incident.severity.toLowerCase()}>
              <td>{incident.timestamp}</td>
              <td>{incident.ip}</td>
              <td>{incident.event}</td>
              <td>{incident.severity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
