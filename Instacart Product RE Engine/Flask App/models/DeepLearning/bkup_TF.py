import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn 
import json
import pickle

hm_epochs = 150
batch_size = 500
num_steps = 10
state_size = 200
vocab_size = 11207

# Placeholders
x = tf.placeholder(tf.int32, [None, num_steps]) # [batch_size, num_steps]
seqlen = tf.placeholder(tf.int32, [None])
y = tf.placeholder(tf.int32, [None, num_steps])


model_path = "./models/DeepLearning/model_data/"
model_path = "./model_data/"






def get_recommendations(cart_items):
    cart_items = [json.loads(cart_items)]
    print(cart_items)
    with open(model_path+'embeddings.txt','rb') as fp:
        embeddings = pickle.load(fp)
    with open (model_path+'words.txt', 'rb') as fp:
        wordlist = pickle.load(fp)
    wordlist.append('UNKNOWN_TOKEN')
    embeddings = np.vstack([embeddings, np.zeros(200)])
    word_to_index = dict([(w,i) for i,w in enumerate(wordlist)])
    test_prod_embeds = [[word_to_index[prod] for prod in bucket] for bucket in cart_items ]
    print(test_prod_embeds)    
    test_x_padded = []
    max_length =  10
    for row in test_prod_embeds:    
        print(row)
        if len(row) <= max_length:
            test_x_padded.append(row + [word_to_index['UNKNOWN_TOKEN']] * (max_length - len(row)))
        else :
            test_x_padded.append(test_prod_embeds[:10])
    print(test_x_padded)
    feed_dict={x: test_x_padded}
    #feed_dict={x: tt}
    sess=tf.Session()
    #First let's load meta graph and restore weights
    saver = tf.train.import_meta_graph(model_path+'model.meta')
    saver.restore(sess,tf.train.latest_checkpoint(model_path))
    sess.run(tf.global_variables_initializer())
    graph = tf.get_default_graph()

    op_to_restore = graph.get_tensor_by_name("logits:0")
    results = sess.run(op_to_restore,feed_dict)
    print("These are results:", results)
    results = np.reshape(results, [len(test_x_padded), num_steps, vocab_size])
    r1= results.argmax(axis=2)
    for pre in (r1[:10]):
        print("Starts")
        print("\ny': These are the predictions made \n%s" % (wordlist[pre[-1]] ))
        #print("\ny': These are the predictions made \n%s" % (",".join([wordlist[x] for x in pre])))
        #print("\ny These are the ground truths :\n%s" % (",".join([wordlist[x] for x in the])))
        print("End\n")
    return  ["a","b"]

print(get_recommendations('["Milk"]'))