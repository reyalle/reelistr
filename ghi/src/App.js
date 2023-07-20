import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import Nav from "./navigation/Nav.js";
import Home from "./pages/Home.js";
import LoginForm from "./components/Login.js";
import MovieDetails from "./pages/MoviesDetails.js";
import Profile from "./pages/Profile.js";
import Collections from "./components/Collections.js";
import Watchlist from "./pages/Watchlist.js";
import SignUpForm from "./components/Signup.js";
import ComingSoon from "./components/ComingSoon.js";
import Trending from "./components/Trending.js";
import Reviews from "./components/Reviews.js";
import CollectionDetail from "./pages/CollectionDetail";


function App() {

  const baseUrl = process.env.REACT_APP_API_HOST

  return (
    <BrowserRouter>
      <AuthProvider baseUrl={baseUrl}>
        <Nav />
        <div>
          <Routes>
            <Route path="user">
            </Route>
            <Route path="profile">
              <Route path="collections" element={<Collections />} />
              <Route path=":collection_id" element={<CollectionDetail />} />
            </Route>
            <Route path="watchlist" element={<Watchlist />} />
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/movies">
              <Route path=":movie_id" element={<MovieDetails />} />
            </Route>
            {/* <Route path="/profile" element={<Profile />} /> */}

            {/* <Route path="/watchlist" element={<Watchlist />} /> */}
            <Route path="/signup" element={<SignUpForm />} />
            <Route path="/comingsoon" element={<ComingSoon />} />
            <Route path="/trending" element={<Trending />} />
            <Route path="/reviews" element={<Reviews />} />

          </Routes>

        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;

{
  /* <ErrorNotification error={error} />
<Construct info={launchInfo} /> */
}
