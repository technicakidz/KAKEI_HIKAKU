import React from 'react';
import './App.css';
import Axios from 'axios';

//function App() {
export class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>input area</h1>
          <form onSubmit={this.handleSubmit}>
            <label>
              <textarea name="text" cols="60" rows="4" value={this.state.value} onChange={this.handleChange} />
            </label>
            <br/>
            <input type="submit" value="run" />
          </form>
        </header>
      </div>
    );
  }

// TODO:  core.py の計算ロジックに送信する修正
  wakati = text => {
    console.log("input text >>"+text)
    Axios.post('http://127.0.0.1:5000/wakati', {
      post_text: text
    }).then(function(res) {
      alert(res.data.result);
    })
  };

  handleSubmit = event => {
    this.wakati(this.state.value)
    event.preventDefault();
  };

  handleChange = event => {
    this.setState({ value: event.target.value });
  };
}

export default App;