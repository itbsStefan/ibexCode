import logo from './logo.svg';
import './App.css';

function App() {
  const myFunction = (event) => {
    alert('OKAY');
  };
  const myHover = (event) => {
    console.log("HOVER");
    console.log(event);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <p>Klasse Berlin 2024 Januar</p>
        <p>
          <strong>Hallo Welt !</strong>
        </p>
        
        <button onClick={event => myFunction(event)}>Klick mich</button>
        <button
          onClick={myFunction}
          onMouseEnter={event => myHover(event)}
        >Klick mich 2</button>
      </header>
    </div>
  );
}

export default App;
