import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../config/settings';
import Navigation from '../Navigation';


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
                <Navigation />
                <div className="container">
                    <h1> Home </h1>
                </div>
            </div>
        )
    }
}

export default Home;