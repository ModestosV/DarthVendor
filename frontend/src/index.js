import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {HashRouter as Router, Route} from 'react-router-dom';
import {createStore, applyMiddleware} from 'redux';  
import {Provider} from 'react-redux';  
import thunk from 'redux-thunk';
import rootReducer from './reducers';
import Login from './components/Login';
import AdminRoutes from './components/Admin/routes';
import MerchantRoutes from './components/Merchant/routes';

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

store.subscribe(() => console.log('store', store.getState()));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <div>                         
                <Route exact path="/login" component={Login}/>     
                <Route path="/admin" component={AdminRoutes}/>
                <Route path="/" component={MerchantRoutes}/>
            </div>
        </Router>
    </Provider>,
    document.getElementById('root')
)

