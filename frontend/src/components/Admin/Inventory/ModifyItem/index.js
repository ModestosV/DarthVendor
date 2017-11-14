import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';
import './modifyitem.scss'

class ModifyItem extends Component {

    constructor(props) {
        super(props);

        this.state = {

        }
    }

    confirmModifications() {

        let data = this.state;

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/modifyItemSpec`,
            data: data,
            headers: {
                Authorization: "Token " + JSON.parse(localStorage.activeUser).token
            },
            withCredentials: true
        })
        .then(response => {
            console.log('item modified');
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
        this.props.closeModal();

    }

    // set state on spec value change
    handleChange(event){
        this.setState({[event.target.name]: event.target.value});
    }

    // display specs of selected item
    displaySpecs() {
            return (
                <div>
                    {Object.keys(this.props.item).map((name,index) => {

                        if(typeof this.props.item[name] != 'object' && !name.includes('Format') ){
                            return (
                                <div className="form-group row" key={index}>
                                    <label htmlFor={name} className="col-sm-2 col-form-label"><strong>{name}</strong></label>
                                    <div className="col-sm-10">
                                        <input type="text" className="form-control" id={name}  name={name} onChange={ (e) => this.handleChange(e) } placeholder={this.props.item[name]}/>
                                    </div>
                                </div>
                            );
                        }
                    })
                    }
                </div>
            );
    }

    handleQuantity(e) {
        this.setState({addQuantity: e.target.value});
    }

    addQuantity() {
        let data = this.state;
        axios({
            method: 'post',
            url: `${settings.API_ROOT}/addQuantity`,
            data: data,
            withCredentials: true
        })
        .then(response => {
            swal({
                text: "Quantity Added!",
                icon: "success",
                button: "Ok",
            });
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

    componentWillMount() {
        this.state = this.props.item;
        console.log(localStorage);

        const {dispatch, history} = this.props;

        // Redirect if user is not logged in
        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);

            if (activeUser.isAdmin === false) {
                // Redirect to merchant home page
                history.push('/');
            }
        }
    }

    render() {
        console.log(this.state);
        return (
            <div>
                <label><strong>Add Quantity</strong></label><br />
                <input className="input--add mr-2" type="number" min="0" onChange={(e) => this.handleQuantity(e)}/>

                <button className="ui blue button" onClick={() => {this.addQuantity()}}>
                    <i className="fa fa-plus"></i> Add 
                </button>
  
                <hr />
                { this.displaySpecs() }
                <div className="mb-5">
                    <button className="ui green button float-right" onClick={() => {this.confirmModifications()}}>Confirm</button>
                </div>
            </div>
        )
    }
}

export default ModifyItem;
