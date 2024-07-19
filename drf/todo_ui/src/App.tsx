import Home_Page from './pages/homepage'
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home_Page />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
