import React, { Component, Fragment } from "react";
import { Header, Divider, Form, Button, Message } from "semantic-ui-react";

import { ENDPOINTS, axios } from "../config";
import { extractError, randomId } from "../helpers";

class AddMovie extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isSubmitting: false, 
      title: "",
      genres: "",
      actors: "", 
      hasErrors: false,
      formErrors: []
    };
  }

  onSubmit = (e) => {
    const { title, genres, actors } = this.state;
    const { addRecentMovie } = this.props;

    // Form validation
    if (!(title.length)) {
      this.setState({
        hasErrors: true,
        formErrors: [
          "Movie title is required."
        ]
      });

      return;
    }

    this.setState({
      isSubmitting: true
    });

    // URL encoded
    const params = new URLSearchParams();
    params.append('title', title);
    params.append('genres', genres);
    params.append('actors', actors);

    // Create the movie
    axios.post(
      ENDPOINTS.movies,
      params
    ).then(resp => {

      this.setState({
        title: "",
        genres: "",
        actors: "",
        isSubmitting: false,
        hasErrors: false,
        formErrors: []
      });

      // Trigger parents addRecentMovie to update recent list
      addRecentMovie({
        id: randomId(),
        title,
        created_at: new Date()
      });

    }).catch(err => {
      const error = extractError(err);

      this.setState({
        hasErrors: true,
        formErrors: [
          error
        ],
        isSubmitting: false
      });
    });

  }

  handleTitle = (e) => {
    this.setState({
      title: e.target.value
    });
  }

  handleGenres = (e) => {
    this.setState({
      genres: e.target.value
    });
  }

  handleActors = (e) => {
    this.setState({
      actors: e.target.value
    });
  }

  render() {
    const { hasErrors, formErrors, isSubmitting, title, genres, actors } = this.state;

    return (
      <Fragment>
        <Header>Add Movie</Header>
        <Divider />

        <Form size="large" onSubmit={this.onSubmit} error={hasErrors}>
          <Form.Input placeholder="Movie title" onChange={this.handleTitle} value={title} />
          <Form.Input placeholder="Genres ex. drama,romance,action" onChange={this.handleGenres} value={genres} />
          <Form.Input placeholder="Actors ex. Bruce Willis,Kate Winslet" onChange={this.handleActors} value={actors} />

          <Message
            error
            header="Oops, something's going wrong!"
            list={formErrors}
          />

          <Button color="green" size="large" loading={isSubmitting}>
            Add Movie
          </Button>
        </Form>
      </Fragment>
    )
  }
};

export default AddMovie;
