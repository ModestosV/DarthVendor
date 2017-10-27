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

    handleForm() {

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
            console.log('item added');
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

    displaySpecs() {
            return (                
                <div>
                    {Object.keys(this.props.item).map((name,index) => {
                        console.log(this.props.item[name]);
                        return (
                            <p key={index}>{name}: {this.props.item[name]}</p>
                        );
                    })
                    }
                </div>  
            );
    }

    componentWillMount() {
        console.log(localStorage);
    }

    render() {
        console.log(this.props);
        return (
            <div>
                <div className="pusher">

                    <div className="container p-0 mt-4">
                    <h1>Modify Item</h1>
                    { this.displaySpecs() }
                    </div>
               
                </div>
            </div>
        )
    }
}

export default ModifyItem;
