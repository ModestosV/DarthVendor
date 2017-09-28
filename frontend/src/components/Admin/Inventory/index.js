import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';

class Inventory extends Component {    

    componentWillMount() {  
        const {history} = this.props;      
        console.log(localStorage);
        
        if (!localStorage.activeUser) {
            history.push('/login');
        }
    }
    
    render() {

        return (
            <div>
                <Sidebar />

                <div className="col-md-10 float-left col px-5 pl-md-2 pt-2 main">
                    <a href="#" data-target="#sidebar" data-toggle="collapse"><i className="fa fa-navicon fa-2x py-2 p-1"></i></a>
                    <div className="page-header">
                        <h5>This is the inventory page and it should show all the products.</h5>
                        <br />
                        <br />
                        <h5>There should be an add new product button that opens a modal?</h5>
                    </div>
                </div>


            </div>
        )
    }
}

export default Inventory;