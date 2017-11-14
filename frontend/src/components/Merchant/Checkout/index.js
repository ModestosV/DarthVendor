import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';

class Checkout extends Component {

  constructor(props) {
    super(props);
    this.state = {
    }
  }

  componentWillMount() {
    const {history} = this.props;
    console.log(localStorage);
    if (!localStorage.activeUser) {
        history.push('/login');
    }
  }

  render() {
    const self = this;

    var history = <Link to={`/return`} >history</Link>;

    return (
      <div>
        <Navigation />
        <div className="justify-content-md-center row">
          <div>
            <h1> Purchase succesfull <i className="fa fa-check" aria-hidden="true"></i></h1>
            <div> Please visit your {history} if you wish to return your items.</div>
          </div>
        </div>
      </div>
    )
  }
}

export default Checkout;