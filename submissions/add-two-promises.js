// https://leetcode.com/problems/add-two-promises

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const [result1, result2] = await Promise.all([promise1, promise2]);
        
        // Sum the results
    const sum = result1 + result2;
        
        // Return a new promise that resolves with the sum
    return Promise.resolve(sum);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */