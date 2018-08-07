import React, { Fragment } from "react";
import { Header, Divider } from "semantic-ui-react";

import ItemList from "../components/ItemList";

const Actors = () => {
  return (
    <Fragment>
      <Header>Actors</Header>
      <Divider />

      <ItemList resourceKind={"actors"} />
    </Fragment>
  );
};

export default Actors;
