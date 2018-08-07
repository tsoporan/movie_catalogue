import React, { Fragment, Component } from "react";
import { Header, Divider } from "semantic-ui-react";

import AddMovie from "../components/AddMovie";
import ItemList from "../components/ItemList";

class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {
      recentMovies: []
    };
  }

  addRecentMovie(movie) {
    this.setState({
      recentMovies: [movie, ...this.state.recentMovies]
    });
  }

  render() {
    const { recentMovies } = this.state;

    return (
      <Fragment>
        <AddMovie addRecentMovie={this.addRecentMovie.bind(this)} />

        <Header>Recently Added</Header>
        <Divider />

        <ItemList
          resourceKind={"movies"}
          limit={3}
          defaultItems={recentMovies}
        />
      </Fragment>
    );
  }
}

export default Home;
