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
                <div>
                    {this.displaySpecs}
                    <div className="form-group">
                        <select className="form-control">
                            <option> {this.state.item.type}, {this.state.item.modelNumber} </option>
                        </select>
                    </div>
                </div>

                <div className="mb-5">
                    <button  className="ui green button float-right"  onClick={() => {this.confirmModifications()}}>Confirm</button>
                </div>

            </div>


        )
    }
}
export default DeleteItem;
