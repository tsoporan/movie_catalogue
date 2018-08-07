import React, { Component, Fragment } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import { Container, Menu } from "semantic-ui-react";

import Home from "./pages/Home";
import Genres from "./pages/Genres";
import Actors from "./pages/Actors";
import Movies from "./pages/Movies";
import MovieDetail from "./pages/MovieDetail";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Router>
          <div>
            <Menu fixed="top" inverted>
              <Container>
                <Menu.Item as={Link} to="/" header>
                  <h1 style={logoStyle}>MovieCatalogrrr</h1>
                </Menu.Item>
                <Menu.Item as={Link} to="/genres" header>
                  Genres
                </Menu.Item>
                <Menu.Item as={Link} to="/actors" header>
                  Actors
                </Menu.Item>
                <Menu.Item as={Link} to="/movies" header>
                  Movies
                </Menu.Item>
              </Container>
            </Menu>

            <Container style={{ marginTop: "7em " }}>
              <Route exact path="/" component={Home} />
              <Route path="/genres" component={Genres} />
              <Route path="/actors" component={Actors} />
              <Route exact path="/movies" component={Movies} />
              <Route path="/movies/:movieId" component={MovieDetail} />
            </Container>
          </div>
        </Router>
      </Fragment>
    );
  }
}

const logoStyle = {
  fontFamily: "Pacifico",
  fontWeight: "normal",
  color: "#fff"
};

export default App;
