import axios from 'axios';
import React, {Component} from 'react';
import { withRouter } from 'react-router';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';
import './modifyitem.scss'

class ModifyItem extends Component {

    constructor(props) {
        super(props);
        this.state = {}
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
            swal({
                text: "Item Spec Modified!",
                icon: "success",
                button: "Ok",
            })
            .then(() => {
                window.location.reload()
            })
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

    // set model number spec value 
    handleModelNumberChange(event) {
        this.handleChange(event);

        if(/^[a-zA-Z0-9]*$/.test(event.target.value)) {
            this.setState({errorModelNumber: false});
            this.setState({noError: false});
        }else{
            this.setState({errorModelNumber: true});
            this.setState({noError: true});
        }
    }

    handleWeightChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorWeight: false});
            this.setState({noError: false});
        }else{
            this.setState({errorWeight: true});
            this.setState({noError: true});
        }
    }

    handlePriceChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorPrice: false});
            this.setState({noError: false});
        }else{
            this.setState({errorPrice: true});
            this.setState({noError: true});
        }        
    }

    handleSizeChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorSize: true});
            this.setState({noError: true});
        }        
    }

    handleRamSizeChange(event) {
        this.handleChange(event);

        if(/^[0-9]*$/.test(event.target.value)) {
            this.setState({errorRamSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorRamSize: true});
            this.setState({noError: true});
        }          
    }

    handleNumCoresChange(event) {
        this.handleChange(event);

        if(/^[0-9]*$/.test(event.target.value)) {
            this.setState({errorNumCores: false});
            this.setState({noError: false});
        }else{
            this.setState({errorNumCores: true});
            this.setState({noError: true});
        }          
    }

    handleHDSizeChange(event) {
        this.handleChange(event);

        if(/^[0-9]*$/.test(event.target.value)) {
            this.setState({errorHDSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorHDSize: true});
            this.setState({noError: true});
        }          
    }

    handleDXChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDX: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDX: true});
            this.setState({noError: true});
        }          
    }

    handleDYChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDY: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDY: true});
            this.setState({noError: true});
        }          
    }

    handleDZChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDZ: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDZ: true});
            this.setState({noError: true});
        }          
    }
    // display specs of selected item
    displaySpecs() {
        let input = null;

        let modelNumber, weight, price, size, ramSize, numCores, hardDriveSize, dx, dy, dz;
        modelNumber = weight = price = size = ramSize = numCores= hardDriveSize = dy = dx = dz = "form-control";

        let modelNumberMsg, weightMsg, priceMsg, sizeMsg, ramSizeMsg, numCoresMsg, hardDriveSizeMsg, dxMsg, dyMsg, dzMsg;
        modelNumberMsg  = weightMsg = priceMsg = sizeMsg = ramSizeMsg = numCoresMsg = hardDriveSizeMsg = dxMsg = dyMsg = dzMsg = "list-group-item hidden";

        let errorCSS = "form-control input--error";
        let errorMsgCSS = "list-group-item";

        if (this.state.errorModelNumber){
            modelNumber = errorCSS;
            modelNumberMsg = errorMsgCSS;
        }
        if (this.state.errorWeight) {
            weight = errorCSS;
            weightMsg = errorMsgCSS;
        }
        if (this.state.errorPrice) {
            price = errorCSS;
            priceMsg = errorMsgCSS;
        }
        if (this.state.errorSize) {
            size = errorCSS;
            sizeMsg = errorMsgCSS;
        }
        if (this.state.errorRamSize) {
            ramSize = errorCSS;
            ramSizeMsg = errorMsgCSS;
        }
        if(this.state.errorNumCores) {
            numCores = errorCSS;
            numCoresMsg = errorMsgCSS;
        }
        if(this.state.errorHDSize) {
            hardDriveSize = errorCSS;
            hardDriveSizeMsg = errorMsgCSS;
        }
        if(this.state.errorDX) {
            dx = errorCSS;
            dxMsg = errorMsgCSS;
        }
        if(this.state.errorDY) {
            dy = errorCSS;
            dyMsg = errorMsgCSS;
        }
        if(this.state.errorDZ) {
            dz = errorCSS;
            dzMsg = errorMsgCSS;
        }
        return (
            <div>
                <div className="error--message mb-2 mt-0">
                    <ul className="list-group">
                        <li className={modelNumberMsg}>Invalid Model Number</li>
                        <li className={weightMsg}>Invalid Weight </li>
                        <li className={priceMsg}>Invalid Price </li>
                        <li className={sizeMsg}>Invalid Size </li>
                        <li className={ramSizeMsg}>Invalid RAM Size </li>
                        <li className={numCoresMsg}>Invalid Number of Cores </li>
                        <li className={hardDriveSizeMsg}>Invalid HD Size </li>
                        <li className={dxMsg}>Invalid DX </li>
                        <li className={dyMsg}>Invalid DY </li>
                        <li className={dzMsg}>Invalid DZ </li>
                    </ul>
                </div>
                {Object.keys(this.props.item).map((name,index) => {
                    if(typeof this.props.item[name] != 'object' && !name.includes('Format') && name !== "quantity"){
                        if(name === "modelNumber") {
                            input = <input type="text"
                                        className={modelNumber}
                                        disabled
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleModelNumberChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "weight") {
                            input = <input type="text"
                                        className={weight}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleWeightChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "price") {
                            input = <input type="text"
                                        className={price}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handlePriceChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "size") {
                            input = <input type="text"
                                        className={size}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleSizeChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "ramSize") {
                            input = <input type="text"
                                        className={ramSize}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleRamSizeChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "numCores") {
                            input = <input type="text"
                                        className={numCores}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleNumCoresChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "hardDriveSize") {
                            input = <input type="text"
                                        className={hardDriveSize}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleHDSizeChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "dx") {
                            input = <input type="text"
                                        className={dx}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleDXChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "dy") {
                            input = <input type="text"
                                        className={dy}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleDYChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "dz") {
                            input = <input type="text"
                                        className={dz}
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleDZChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else if (name === "type") {
                            input = <input type="text"
                                        className="form-control"
                                        id={name}
                                        disabled
                                        name={name}
                                        onChange={ (e) => this.handleChange(e) }
                                        placeholder={this.props.item[name]}/>
                        } else {
                            input = <input type="text"
                                        className="form-control"
                                        id={name}
                                        name={name}
                                        onChange={ (e) => this.handleChange(e) }
                                        placeholder={this.props.item[name]}/>
                        }
                        return (
                            <div className="form-group row" key={index}>
                                <label htmlFor={name} className="col-sm-2 col-form-label"><strong>{name}</strong></label>
                                <div className="col-sm-10">
                                     {input}
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
            })
            .then(() => {
                window.location.reload()
            })
            
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
        this.setState({noError: false});
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
                {console.log(this.state.noError)}
                   {this.state.noError === true && 
                        <button className="ui green button disabled float-right">Confirm</button>
                    }

                    {this.state.noError === false && 
                        <button className="ui green button float-right" onClick={() => {this.confirmModifications()}}>Confirm</button>
                    }

                </div>
            </div>
        )
    }
}

export default withRouter(ModifyItem);
