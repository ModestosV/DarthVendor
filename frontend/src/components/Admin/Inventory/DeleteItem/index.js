import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';

class DeleteItem extends Component {
    constructor(props) {
        super(props);
        this.state = {
            item: []
        }
    }
    // add deletions to UOW
    confirmDeletion() {
        let data = this.state;
        this.props.closeDeleteModal();
    }

    // display specs of selected item
    displaySpecs() {

    }
    // get item to delete
    componentWillMount() {
        this.setState({item: this.props.item});

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/getItemIDs`,
            data: this.props.item,
            withCredentials: true
        }).then(result => {
            console.log(result);
        });
    }
    render() {
        console.log(this.state.item);
        return (
            <div>
                <div className="pusher">
                    <h1>Delete Item</h1>
                    {this.displaySpecs}
                    <button onClick={this.props.closeDeleteModal}>Close Modal</button>
                    <button onClick={() => {this.confirmModifications()}}>Confirm</button>
                    <select>
                        <option> {this.state.item.type}, {this.state.item.modelNumber} </option>
                    </select>
                </div>
            </div>
        )
    }
}
export default DeleteItem;
