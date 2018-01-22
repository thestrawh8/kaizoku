
.. title: Competitive Programming Trajectory
.. slug: 
.. date: 2018-01-21 12:06:09 UTC
.. tags: Solutions, Practice
.. category: Programming
.. link: 
.. description: 
.. type: text

## Leet Code

* **Problem : 617 - "Merge Two Binary Trees"**

```c++
class Solution {
public:
    TreeNode* mergeTrees(TreeNode *t1,TreeNode *t2) {
        
        if(t1==NULL && t2==NULL){
            return NULL;
        }
        else{
            if(t1==NULL){
                t1 = t2;
            }
            else if(t1 !=NULL && t2 !=NULL){
                t1->val = t1->val + t2->val;
                t1->left = mergeTrees(t1->left,t2->left);
                t1->right = mergeTrees(t1->right,t2->right);
            }
            return t1;
            }
        }
        
};
```
<!-- TEASER_END -->
* **Problem : 557 - "Reverse words in a String"**

Learned about input stringstream have to check soem more regarding stringstream operation.

```c++
class Solution {
public:
    string reverseWords(string s) {
        std::istringstream tmp(s);
        std::stringstream ss;
        std::vector<std::string> collection((std::istream_iterator<std::string>(tmp)),std::istream_iterator<std::string>());
        for (std::vector<std::string>::iterator it=collection.begin();it!=collection.end();it++){
            std::reverse((*it).begin(),(*it).end());
            ss << *it << " ";  
        }
    std::string result = ss.str();
    result.pop_back();
    return result;
    }
};
```

* **Problem : 535 - "Encode and Decode TinyURL"**

Learned about find operation in unordered::map container it returns an `const_iterator` which points to the given key. If the map doesn't have the key then it will return `map.end()`.

```c++
class Solution {
public:
    std::unordered_map<std::string,std::string> urlencodebuck;
    std::unordered_map<std::string,std::string> urldecodebuck;
    std::string alphanum = "abcdefghijklmnopqrstuvwxyz0123456789";
    std::unordered_map<std::string,std::string>::const_iterator check;

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        check = urlencodebuck.find(longUrl);
        if(check != urlencodebuck.end())
            return urlencodebuck[longUrl];
        else{
            std::string shortUrl = "";
            for(int i=0;i<6;i++){
                shortUrl = shortUrl + alphanum[(rand() % 36)];
            }
            urlencodebuck[longUrl] = shortUrl;
            urldecodebuck[shortUrl] = longUrl;
            return urlencodebuck[longUrl];
        }
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return urldecodebuck[shortUrl];
    }
};
```

