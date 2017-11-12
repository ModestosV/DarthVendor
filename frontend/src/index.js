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
import AdminInventory from './components/Admin/Inventory';
import AdminInventoryAddItem from './components/Admin/Inventory/AddItem';
import MerchantHome from './components/Merchant/Catalog';
import MerchantReturn from './components/Merchant/Return';

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

store.subscribe(() => console.log('store', store.getState()));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <div>
                <Route exact path="/" component={MerchantHome}/>
                <Route exact path="/return" component={MerchantReturn}/>
                <Route exact path="/admin/" component={AdminHome}/>
                <Route exact path="/admin/update" component={AdminInventory}/>
                <Route exact path="/login" component={AdminLogin}/>
                <Route exact path="/admin/add" component={AdminInventoryAddItem}/>
            </div>
        </Router>
    </Provider>,
    document.getElementById('root')
)

