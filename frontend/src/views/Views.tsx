import  React, { useState, useEffect, Fragment } from "react";
import {
  Grid,
  Toolbar,
  AppBar,
  Typography,
  Button
} from "@mui/material"

import MenuButton  from "@mui/material/icons-material/Menu";


const DocumentView = () => {


  return (
    <Fragment>
      <AppBar>
        <Toolbar class="app-toolbar">
           <Typography variant="title">
               App Name
           </Typography>
           <div>
             <Button variant="contained">PDF</Button>
             <Button variant="outlined">Docx</Button>
             <Button variant="contained">Xslx</Button>
           </div>
        </Toolbar>
      </AppBar>
      <div>

      </div>
    </Fragment>
  )
}

export default DocumentView;
