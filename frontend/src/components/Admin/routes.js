import React from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import AdminHome from './Home';
import AdminInventory from './Inventory';
import AdminInventoryAddItem from './Inventory/AddItem';

const AdminRoutes = ({match}) => {
    // console.log(match);
    const routes = (    
        <div>                
            <Route exact path={match.url} component={AdminHome}/>
            <Route exact path={match.url + '/update'} component={AdminInventory}/>
            <Route exact path={match.url + '/add'} component={AdminInventoryAddItem}/>
        </div>
    );

    return routes;
}

export default AdminRoutes;