import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {HashRouter as Router, Route} from 'react-router-dom';
import {createStore, applyMiddleware} from 'redux';  
import {Provider} from 'react-redux';  
import thunk from 'redux-thunk';
import rootReducer from './reducers';
import Login from './components/Login';
import Admin from './components/Admin';
import Home from './components/Home';
import AddItem from './components/Inventory';


const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

store.subscribe(() => console.log('store', store.getState()));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <div>
                <Route exact path="/" component={Home}/>
                <Route exact path="/admin" component={Admin}/>
                <Route exact path="/login" component={Login}/>
                <Route exact path="/inventory" component={AddItem}/>
            </div>
        </Router>
    </Provider>,
    document.getElementById('root')
)