import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
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
          const errorMsg = null;
          let items = results.data.cartItems;
          this.setState({items});
          this.setState({errorMsg});
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
      url: `${settings.API_ROOT}/removeFromCart`,
      data: data,
      withCredentials: true
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

    axios({
        method: 'post',
        url: `${settings.API_ROOT}/confirmPurchase`,
        data: {},
        withCredentials: true
    }).then(() => {
        console.log("checked out");
    })

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
                {item.itemID.itemSpec.modelNumber}, {item.itemID.itemSpec.name}, {item.itemID.serialNumber}
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
                {this.state.items.length < 1 && 
                  <div className="col-sm-12">
                    Shopping cart is empty. <i className="fa fa-frown-o" aria-hidden="true"></i>
                  </div>
                }
                {this.state.items.length >= 1 &&
                  <Link className="btn btn-success float-right col-sm-2 mt-2"
                    to={`/checkout`}
                    onClick={() => this.handleCheckout()}>
                    Checkout
                  </Link>
                }
                </div>
            </div>
        </div>
      </div>
    )
  }
}

export default Cart;
