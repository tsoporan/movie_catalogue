import React, { Fragment } from 'react';
import { Header, Divider } from "semantic-ui-react";

import ItemList from "../components/ItemList";

const Movies = () => {
  return (
    <Fragment>
      <Header>All Movies</Header>
      <Divider />

      <ItemList
        resourceKind={"movies"}
      />
    </Fragment>
  );
};

export default Movies;
