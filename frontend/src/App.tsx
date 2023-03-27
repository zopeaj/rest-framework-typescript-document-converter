import React from 'react';
import { BrowsableRoutes, Routes, Route } from "react-Route-dom"
import PdfConverter from "./views/PdfConverter";
import WordConverter from "./views/WordConveter";
import XsxlConverter from "./views/XsxlConveter";
import DocumentView from "./views/Views";

function App() {
  return (
    <BrowsableRoutes>
      <Routes>
        <Route path exact="*" component={DocumentView} />
        <Route path exact="/pdf-to-word" component={PdfConverter} />
        <Route path exact="/word-to-pdf" component={WordConverter} />
        <Route path exact="/xsxl-to-word" component={XsxlConverter} />
      </Routes>
    </BrowsableRoutes>
  );
}

export default App;
