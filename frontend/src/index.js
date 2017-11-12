import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {HashRouter as Router, Route} from 'react-router-dom';
import {createStore, applyMiddleware} from 'redux';  
import {Provider} from 'react-redux';  
import thunk from 'redux-thunk';
import rootReducer from './reducers';
import AdminHome from './components/Admin/Home';
import AdminInventory from './components/Admin/Inventory';
import AdminInventoryAddItem from './components/Admin/Inventory/AddItem';
import AdminClients from './components/Admin/Clients'
import MerchantHome from './components/Merchant/Catalog';
import Cart from './components/Merchant/Cart';
import Login from './components/Login';
import AdminRoutes from './components/Admin/routes';
import MerchantRoutes from './components/Merchant/routes';
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
                <Route exact path="/login" component={Login}/>     
                <Route path="/admin" component={AdminRoutes}/>
                <Route path="/" component={MerchantRoutes}/>
                
            </div>
        </Router>
    </Provider>,
    document.getElementById('root')
)

