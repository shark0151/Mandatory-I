const express = require("express");
const router = express.Router();
const axios = require("axios");
// set url as constant
const URL = "http://127.0.0.1:8080/time";

/**
 * @swagger
 * tags:
 *   name: Time
 *   description: Show the current time
 */
/**
 * @swagger
 * /time:
 *   get:
 *     summary: Returns the current time as a string
 *     tags: [Time]
 *     responses:
 *       200:
 *         description: The current time
 */
router.get("/", async (req, res, next) => {
  try {
    const response = await axios.get(URL);
    console.log(response.data);
    res.send(response.data);
  } catch (err) {
    next(err);
  }
});

module.exports = router;
