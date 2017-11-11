import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';


class Cart extends Component {    

    constructor(props) {
        super(props);
        this.state = {
            items:[{'modelNumber':'ZZZZZZZ',
            'quantity':46,
            'name':'Razer Desktop',
            'weight':15.0,
            'weightFormat':'lbs',
            'price':2299.99,
            'priceFormat':'CAD',
            'brandName':'RAZER',
            'type':'Desktop',
            'ramSize':16,
            'ramFormat':'GB',
            'processorType':'INTEL',
            'numCores':4,
            'hardDriveSize':2,
            'hardDriveFormat':'TB',
            'dx':15,
            'dy':30,
            'dz':1,
            'dimensionFormat':'INCH'}]
        }
    }

    componentWillMount() {  
        const {history} = this.props;      
        console.log(localStorage);
        
        if (!localStorage.activeUser) {
            history.push('/login');
        }
    }

    componentDidMount() {
        //this.getCatalog();
    }
    
    render() {
        return (
            <div>
                <Navigation />
                <div className="row">
                    <div className="col-md-2"></div>
                    <div className="col-md-8 offset-md-2">
                        <div className="mt-2"> <h1 className="m-0"> Shopping Cart </h1> </div>
                        <div className="card mt-2">
                          <ul className="list-group list-group-flush">
                            <li className="list-group-item">
                                <div className="row"> 
                                    <div className="col-sm-12">
                                        <div> Item 1 </div>
                                    </div>
                                </div>
                            </li>
                            <li className="list-group-item">
                                <div className="row"> 
                                    <div className="col-sm-12">
                                        <div> Item 1 </div>
                                    </div>
                                </div>
                            </li>
                            <li className="list-group-item">
                                <div className="row"> 
                                    <div className="col-sm-12">
                                        <div> Item 1 </div>
                                    </div>
                                </div>
                            </li>
                          </ul>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Cart;