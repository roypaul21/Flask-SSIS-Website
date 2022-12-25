using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ProbeScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        GetComponent<Rigidbody2D>().velocity = new Vector2(-2, 2);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "empty")
        {
            GameScript.ULStatus = "r";
            Destroy(gameObject);
        }

        if (other.tag == GameScript.currentTurn)
        {
            GameScript.ULStatus = "y";
            Destroy(gameObject);
        }

        if (other.tag != GameScript.currentTurn)
        {
            other.tag = gameObject.tag;
        }
    }
}
