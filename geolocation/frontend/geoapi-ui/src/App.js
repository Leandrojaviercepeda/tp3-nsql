import React from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import './App.css';

import Home from './components/Home'
import Client from './components/Client'
import WhereIAm from './components/WhereIAm'

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path='/' render={ () => <Redirect to='/home' component={ Home }/>}/>
        <Route exact path='/home' component={ Home }/>
        <Route exact path='/client' component={ Client }/>
        <Route exact path='/where' component={ WhereIAm }/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
