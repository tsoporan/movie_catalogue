import React, { Fragment} from 'react';
import { Header, Divider } from "semantic-ui-react";

import ItemList from "../components/ItemList";

const Genres = () => {
  return (
    <Fragment>
      <Header>Genres</Header>
      <Divider />

      <ItemList resourceKind={"genres"} />
    </Fragment>

  );
};

export default Genres;
