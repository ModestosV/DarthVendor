import React from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import MerchantHome from './Catalog';
import MerchantReturn from './Return';
import MerchantCart from './Cart';

const MerchantRoutes = ({match}) => {
    // console.log(match);
    const routes = (    
        <div>                
            <Route exact path={match.url} component={MerchantHome}/>
            <Route exact path={match.url + 'return'} component={MerchantReturn}/>  
            <Route exact path={match.url + 'cart'} component={MerchantCart}/>  
        </div>
    );

    return routes;
}

export default MerchantRoutes;