import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';


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
            url: `${settings.API_ROOT}/item`,
            data: data,
            headers: {
                Authorization: "Token " + JSON.parse(localStorage.activeUser).token
            }
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
                        if(typeof this.props.item[name] != 'object'){
                            return (
                                <div key={index}>
                                    {name}: <input type="text" name={name} onChange={ (e) => this.handleChange(e) } placeholder={this.props.item[name]}/>
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
        let data = this.state.addQuantity;
        
        // axios({
        //     method: 'post',
        //     url: `${settings.API_ROOT}/item`,
        //     data: data,
        //     headers: {
        //         Authorization: "Token " + JSON.parse(localStorage.activeUser).token
        //     }
        // })
        // .then(response => {
        //     swal({
        //         text: "Quantity Added!",
        //         icon: "success",
        //         button: "Ok",
        //     });
        // })
        // .catch(error => {
        //     console.log(error);
        //     swal({
        //         title: "Woops!",
        //         text: "Something went wrong!",
        //         icon: "error",
        //         button: "Ok",
        //     });
        // })
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

            if (activeUser.adminPermission === false) {
                // Redirect to merchant home page                
                history.push('merchant');
            }            
        }        
    }

    render() {
        console.log(this.state);
        return (
            <div>
                <div className="pusher">
                    <button onClick={() => {this.confirmModifications()}}>Confirm</button>
                    <div className="container p-0 mt-4">
                    <h1>Modify Item</h1>
                    { this.displaySpecs() }
                    </div>
               
                </div>
                <div>
                    <button onClick={() => {this.addQuantity()}}> Add Quantity</button>
                    <input type="number" min="0" onChange={(e) => this.handleQuantity(e)}/>
                </div>

            </div>
        )
    }
}

export default ModifyItem;
