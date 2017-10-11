import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';

class Home extends Component {    

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

                <div className="pusher">

                    <div className="mt-4 text-center">
                     <h1>Darth Vendor Admin Panel</h1>
                    </div>
              
                </div>

            </div>
     
        )
    }
}

export default Home;