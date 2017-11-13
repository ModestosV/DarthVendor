import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';


class Cart extends Component {

  constructor(props) {
    super(props);
    this.state = {
      items:[],
      errorMsg: null
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
      this.cartItemsList();
  }

  cartItemsList() {
      return axios({
          method:'get',
          url: `${settings.API_ROOT}/viewCart`,   // needs to be change to correct URL
          withCredentials: true
      })
      .then(results => {
          console.log("VIEW CART DATA");
          console.log(results.data);
          const errorMsg = null;
          let items = results.data.cartItems;
          this.setState({items});
          this.setState({errorMsg});
          // console.log(items);
      })
      .catch(error => {
       console.log(error);
       const errorMsg = "Oops, something went wrong while fetching items from shopping cart!";
       this.setState({errorMsg});
     })
  }

  handleDeleteCartItem(row) {
    console.log("unlock item");
    const data = row;

    axios({
      method: 'post',
      url: `${settings.API_ROOT}/cart`, // need to change this
      data: data,
      headers: {
          Authorization: "Token " + JSON.parse(localStorage.activeUser).token
      }
    })
    .then(response => {
      swal({
        text: "Item deleted from cart!",
        icon: "success",
        button: "Ok",
      });

      this.cartItemsList()
    })
    .catch(error => {
      console.log(error);
      swal({
        title: "Woops!",
        text: "Something went wrong!",
        icon: "error",
        button: "Ok",
      });
    })
  }

  handleCheckout() {
    console.log("checking out");
    console.log("unlock cart item");
  }
  render() {
    const self = this;
    
    let cartItems = [];
    self.state.items.map((item, index) => {
        cartItems.push(
          <li key={index}
            className="list-group-item">
            <div className="row">
              <div className="col-sm-11">
                {item.itemID.itemSpec.modelNumber}, {item.itemID.itemSpec.name}
              </div>
              <div className="col-sm-1 text-right">
                <i className="fa fa-times"
                  aria-hidden="true"
                  onClick={() => this.handleDeleteCartItem(item)}>
                </i>
              </div>
            </div>
          </li>
        )        
      }
    )     

    return (
      <div>
        <Navigation />
        <div className="row">
          <div className="col-md-2"></div>
            <div className="col-md-8 offset-md-2">
              <div className="mt-2">
                <h1 className="m-0"> Shopping Cart </h1> </div>
                { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                <div className="card mt-2">
                  <ul className="list-group list-group-flush">
                    {cartItems}
                  </ul>
                </div>
                <div className="justify-content-md-center">
                  <button className="btn btn-success float-right col-sm-2 mt-2"
                    onClick={() => this.handleCheckout()}>
                    Checkout
                  </button>
                </div>
            </div>
        </div>
      </div>
    )
  }
}

export default Cart;
