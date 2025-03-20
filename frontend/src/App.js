import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Dashboard from './Dashboard';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <h1>SentinelGuard</h1>
          <Link to="/">Dashboard</Link>
        </nav>
        <Switch>
          <Route path="/" exact component={Dashboard} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
