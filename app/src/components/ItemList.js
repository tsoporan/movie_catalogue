import React, { Fragment, Component } from 'react';
import { Header, Divider, Loader, Card } from "semantic-ui-react";

import { ENDPOINTS, axios } from "../config";
import { extractError } from"../helpers";

import Item from "./Item";

class ItemList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      error: null,
      items: []
    }
  }

  componentDidMount() {
    const { resourceKind, limit = null }  = this.props;

    const params = new URLSearchParams();
    const endpoint = ENDPOINTS[resourceKind];

    if (limit) {
      params.append('limit', limit);
    }

    this.setState({
      isLoading: true
    });

    // Request resource
    axios.get(
      endpoint,
      {
        params
      }
    )
      .then(resp => {
        const items = resp.data[resourceKind];

        this.setState({
          items,
          isLoading: false
        });

      })
      .catch(err => {
        const error = extractError(err);

        this.setState({
          error
        });

      });
  }

  render() {
    let { items, isLoading, error } = this.state;
    let { resourceKind, defaultItems, limit = null } = this.props;

    // Allow default items to take precedence
    if (defaultItems) {
      if (limit) {
        items = [...defaultItems, ...items].slice(0, limit);
      } else {
        items = [...defaultItems, ...items];
      }
    }

    if (error) {
      return (
        <Fragment>
          Oops, it looks like there was an error!
          {error}
        </Fragment>
      );
    }

    if (isLoading) {
      return (
        <Fragment>
          <Loader active={true} />
        </Fragment>
      );
    } else {
      return (
        <Fragment>
          {items && items.length > 0 ? (
            <Card.Group centered>
              {items.map(item=> <Item key={item.id} item={item} resourceKind={resourceKind} />)}
            </Card.Group>
          ) : (
            <p> No {resourceKind}, please add them first.</p>
          )}
        </Fragment>
      );
    }
  }
};

export default ItemList;
