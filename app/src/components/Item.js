import React, { Fragment } from "react";
import { Card } from "semantic-ui-react";
import moment from "moment";

import { pickColor } from "../helpers";

const Item = (props) => {
  const { item, resourceKind } = props;
  const color = pickColor();
  const parsedDate = item.created_at ? moment(item.created_at).format("YYYY-MM-DD HH:mm") : null;

  let heading;

  switch (resourceKind) {
    case "movies":
      heading = item.title;
      break;
    case "actors":
    case "genres":
      heading = item.name;
      break;
    default:
  }

  return (
    <Fragment>
      <Card color={color}>
        <Card.Content>
          <Card.Header>{heading}</Card.Header>
          {parsedDate && <Card.Meta><span className="date">Added: {parsedDate}</span></Card.Meta> }
          <Card.Description>ID: #{item.id}</Card.Description>
        </Card.Content>
      </Card>
    </Fragment>
  );
};

export default Item;
