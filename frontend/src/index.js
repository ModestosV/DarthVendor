import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {HashRouter as Router, Route} from 'react-router-dom';
import {createStore, applyMiddleware} from 'redux';  
import {Provider} from 'react-redux';  
import thunk from 'redux-thunk';
import rootReducer from './reducers';
import AdminLogin from './components/Admin/Login';
import AdminHome from './components/Admin/Home';
import AdminInventory from './components/Admin/Inventory'
import AdminAddProduct from './components/Admin/Products'

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

store.subscribe(() => console.log('store', store.getState()));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <div>
                <Route exact path="/" component={AdminHome}/>
                <Route exact path="/inventory" component={AdminInventory} />
                <Route exact path="/add" component={AdminAddProduct} />
                <Route exact path="/login" component={AdminLogin}/>
            </div>
        </Router>
    </Provider>,
    document.getElementById('root')
)

