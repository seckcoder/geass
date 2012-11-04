/*
 * IntervalTree, implemented with builder pattern
 */
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;
using std::vector;
template<class OrigDataType>
class TreeNode {
public:
  int l, r;
  TreeNode() {
    l = r = -1;
    orig_vec = NULL;
  }
  TreeNode(int _l, int _r) {
    l = _l;
    r = _r;
  }
  void set_orig_vec(const vector<OrigDataType> *_orig) {
    orig_vec = _orig;
  }
  void fill(int _l, int _r) {
    l = _l;
    r = _r;
  }
  void fill(int _l, int _r, const TreeNode *lc, const TreeNode *rc) {
    fill(_l, _r);
  }
  void print() {
    cout << l << " " << r << endl;
  }
  //virtual bool is_bad(const TreeNode *node) = 0;
protected:
  const vector<OrigDataType> *orig_vec;
};


template<class TheTreeNode, class OrigDataType>
class IntervalTree {
 public:
  IntervalTree() {
    tree = NULL;
    orig_vec = NULL;
  } 

  void build(const vector<OrigDataType> &_orig) {
    tree = new TheTreeNode[2 * _orig.size()];
    orig_vec = &_orig;
    build(0, 0, _orig.size() - 1);
  }

  TheTreeNode *build(int node_idx, int l, int r) {
    TheTreeNode &node = tree[node_idx];
    node.set_orig_vec(orig_vec);
    if (l ==r)  {
      node.fill(l, r, NULL, NULL);
      //cout << node_idx << ":";
      //node.print();
      return &node;
    }
    int mid = ceil((l + r) * 0.5);
    TheTreeNode *lc = build(left_child(node_idx), l, mid - 1);
    TheTreeNode *rc = build(right_child(node_idx), mid, r);
    node.fill(l, r, lc, rc);
    //cout << node_idx << ":";
    //node.print();
    return &node;
  }

  TheTreeNode search(int node_idx, int l, int r) {
    TheTreeNode cur_node = tree[node_idx];
    //cout << node_idx << " " << l << " " << r << endl;
    if (l > r) return TheTreeNode::bad();
    if (cur_node.r < l || cur_node.l > r) return TheTreeNode::bad();
    if (cur_node.r == r && cur_node.l == l) return cur_node;
    TheTreeNode lc = tree[left_child(node_idx)];
    TheTreeNode rc = tree[right_child(node_idx)];
    TheTreeNode lret = search(left_child(node_idx),
                              (std::max)(l, lc.l),
                              (std::min)(r, lc.r));
    //cout << lret << endl;
    TheTreeNode rret = search(right_child(node_idx),
                              (std::max)(l, rc.l),
                              (std::min)(r, rc.r));
    //cout << rret <<endl;
    return TheTreeNode(l, r,
                       (std::min)(lret.tmin, rret.tmin),
                       (std::max)(lret.tmax, rret.tmax));
  }
  int left_child(int root) { return 2*root + 1; }
  int right_child(int root) { return 2*root + 2; }

  private:
   TheTreeNode *tree;  // tree root
   const vector<OrigDataType> *orig_vec;
};
