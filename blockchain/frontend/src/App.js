import './App.css';
import React, { Component } from 'react';
import Status from './components/status'
import Send from './components/send'
import Transactions from './components/transactions'
import axios from 'axios';

/*
import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
*/

const endpoint = '/blockchain/mine_block/';

class App extends Component {
  state = {
    message: "",
    index: 0,
    timestamp: "",
    nonce: 1,
    previous_hash: "0",
    transactions: []
  }

  componentDidMount() {
    axios.get(endpoint)
      .then(res => {
        this.setState({
          message: res.data.message,
          index: res.data.index,
          timestamp: res.data.timestamp,
          nonce: res.data.nonce,
          previous_hash: res.data.previous_hash,
          transactions: res.data.transactions,
        });
      })
  }

  render() {
    return (
      <div className="App">
        <Status />
        <Send />
        <Transactions />
      </div>
    );
  }
}

export default App;
