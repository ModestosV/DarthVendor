import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../config/settings';
import Navigation from '../Navigation';


class Home extends Component {    

    componentWillMount() {        
        console.log(JSON.parse(localStorage.activeUser));
    }
    
    render() {
        return (
            <div>
                <Navigation />
                <div className="container">
                    <h1> Home </h1>
                </div>
            </div>
        )
    }
}

export default Home;