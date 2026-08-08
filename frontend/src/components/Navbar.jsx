import { FaFileAlt } from "react-icons/fa";

function Navbar() {

  return (

    <nav className="navbar">

      <div className="logo">
        <FaFileAlt size={28}/>
        <h2>Case Intake Processor</h2>
      </div>

      <div className="title">
        Case Intake Processor
      </div>

    </nav>

  );

}

export default Navbar;